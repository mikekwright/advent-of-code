# shellcheck shell=bash

readonly AOC_URL="${AOC_URL:-https://adventofcode.com}"
readonly AOC_USER_AGENT="${AOC_USER_AGENT:-aoc-fetch (personal nix flake script)}"
readonly AOC_SESSION_FILE="${AOC_SESSION_FILE:-${XDG_CONFIG_HOME:-$HOME/.config}/aoc/session}"
readonly FIRST_YEAR=2015
readonly LAST_DAY=25

usage() {
  cat <<EOF
Usage: aoc-fetch [--year YEAR] [--day DAY] [--next] [--force]

Saves the puzzle description to <year>/day<N>/README.md and downloads your
puzzle input to <year>/day<N>/input.txt. Existing files are not overwritten
unless --force is given. Part two of a puzzle is only included when the
session cookie is available and part one has been solved.

  (no arguments)   fetch today's puzzle (only valid while an event is running)
  -y, --year YEAR  event year, defaults to the most recent event
  -d, --day DAY    day of the event (1-$LAST_DAY)
  -n, --next       fetch the first day of the year that has no input yet
  -f, --force      download the README again, for example to add part two
  -h, --help       show this help

Environment:
  AOC_SESSION       session cookie from adventofcode.com (input and part two)
  AOC_SESSION_FILE  file holding the session cookie [$AOC_SESSION_FILE]
  AOC_ROOT          repository root, defaults to the git top level
  AOC_USER_AGENT    user agent sent to adventofcode.com
  AOC_URL           base url [$AOC_URL]
EOF
}

die() {
  echo "aoc-fetch: $*" >&2
  exit 1
}

aoc_date() {
  TZ=EST5 date "+$1"
}

latest_event_year() {
  local year month
  year=$(aoc_date %Y)
  month=$(aoc_date %-m)
  if ((month == 12)); then
    echo "$year"
  else
    echo $((year - 1))
  fi
}

todays_day() {
  local month day
  month=$(aoc_date %-m)
  day=$(aoc_date %-d)
  if ((month != 12 || day > LAST_DAY)); then
    die "no event is running today, pass --next or --year/--day (see --help)"
  fi
  echo "$day"
}

repo_root() {
  if [[ -n "${AOC_ROOT:-}" ]]; then
    echo "$AOC_ROOT"
  else
    git rev-parse --show-toplevel 2>/dev/null || pwd
  fi
}

day_dir() {
  local year_dir=$1 day=$2 padded candidate
  padded=$(printf '%02d' "$day")
  for candidate in "day$day" "day-$padded" "$padded"; do
    if [[ -d "$year_dir/$candidate" ]]; then
      echo "$year_dir/$candidate"
      return
    fi
  done
  echo "$year_dir/day$day"
}

has_input() {
  [[ -e "$1/input.txt" || -e "$1/puzzle-input.txt" ]]
}

next_day() {
  local year_dir=$1 day
  for ((day = 1; day <= LAST_DAY; day++)); do
    if ! has_input "$(day_dir "$year_dir" "$day")"; then
      echo "$day"
      return
    fi
  done
  die "every day in $year_dir already has an input"
}

session_token() {
  local token=""
  if [[ -n "${AOC_SESSION:-}" ]]; then
    token=$AOC_SESSION
  elif [[ -r "$AOC_SESSION_FILE" ]]; then
    token=$(tr -d '[:space:]' <"$AOC_SESSION_FILE")
  fi
  if [[ -n "$token" && ! "$token" =~ ^[0-9a-fA-F]+$ ]]; then
    die "the session cookie does not look like a hex token"
  fi
  echo "$token"
}

download() {
  local url=$1 session=${2:-}
  local -a options=(--fail --silent --show-error --location --user-agent "$AOC_USER_AGENT")
  if [[ -n "$session" ]]; then
    curl "${options[@]}" --config - "$url" <<<"cookie = \"session=$session\""
  else
    curl "${options[@]}" "$url"
  fi
}

puzzle_description() {
  local url=$1 session page
  session=$(session_token)
  page=$(download "$url" "$session") || die "puzzle $url is not available"
  sed -n '/<article class="day-desc">/,/<\/article>/p' <<<"$page" |
    pandoc --from html --to gfm-raw_html --wrap auto --columns 80 |
    sed -E 's/^## --- (.*) ---$/## \1/'
}

write_readme() {
  local readme=$1 year=$2 day=$3 url=$4 description
  description=$(puzzle_description "$url")
  [[ -n "$description" ]] || die "could not find the puzzle description on $url"
  mkdir -p "$(dirname "$readme")"
  cat >"$readme" <<EOF
# Advent of Code - $year - Day $day

This problem is taken from the Advent of Code site on
[day$day]($url)

$description

## Source

The puzzle text above was written by Eric Wastl for
[Advent of Code]($AOC_URL) and was downloaded from
<$url>.
It is copyright Advent of Code and is kept here for personal reference only,
it is not to be redistributed.
EOF
  echo "created $readme"
}

write_input() {
  local input=$1 url=$2 session
  session=$(session_token)
  if [[ -z "$session" ]]; then
    echo "skipped $input, set AOC_SESSION or create $AOC_SESSION_FILE to download it" >&2
    return
  fi
  download "$url/input" "$session" >"$input.partial" || {
    rm -f "$input.partial"
    die "could not download $url/input, is the session cookie still valid?"
  }
  mv "$input.partial" "$input"
  echo "created $input"
}

main() {
  local year="" day="" next=false force=false
  while (($# > 0)); do
    case $1 in
      -y | --year)
        year=${2:-}
        shift 2 || die "--year needs a value"
        ;;
      -d | --day)
        day=${2:-}
        shift 2 || die "--day needs a value"
        ;;
      -n | --next)
        next=true
        shift
        ;;
      -f | --force)
        force=true
        shift
        ;;
      -h | --help)
        usage
        exit 0
        ;;
      *)
        usage >&2
        die "unknown argument: $1"
        ;;
    esac
  done

  [[ -n "$year" ]] || year=$(latest_event_year)
  [[ "$year" =~ ^[0-9]{4}$ ]] || die "invalid year: $year"
  ((year >= FIRST_YEAR)) || die "Advent of Code started in $FIRST_YEAR"

  local year_dir
  year_dir="$(repo_root)/$year"

  if [[ -n "$day" && "$next" == true ]]; then
    die "--day and --next cannot be combined"
  elif [[ "$next" == true ]]; then
    day=$(next_day "$year_dir")
  elif [[ -z "$day" ]]; then
    day=$(todays_day)
  fi
  [[ "$day" =~ ^[0-9]{1,2}$ ]] || die "invalid day: $day"
  day=$((10#$day))
  ((day >= 1 && day <= LAST_DAY)) || die "day must be between 1 and $LAST_DAY"

  local dir url
  dir=$(day_dir "$year_dir" "$day")
  url="$AOC_URL/$year/day/$day"

  if [[ "$force" == true || ! -e "$dir/README.md" ]]; then
    write_readme "$dir/README.md" "$year" "$day" "$url"
  fi
  if ! has_input "$dir"; then
    write_input "$dir/input.txt" "$url"
  fi
}

main "$@"
