Advent of Code
==================================

Well, I am resurrecting this repository in 2025 as being a manager leaves nearly
no time for development during work these days.  I am going to turn 2025 into
the year of advent, using each month to represent a specific year of the advent
of code.

Since I am starting this in Feburary though, so for February I am going to
work on both year 2015 and year 2016 before moving forward with the rest of the
years of advent of code.

Lets get started!

Years
------------------------------------

* [2015](https://adventofcode.com/2015)
* [2016](https://adventofcode.com/2016)
* [2017](https://adventofcode.com/2017)
* [2018](https://adventofcode.com/2018)
* [2019](https://adventofcode.com/2019)
* [2020](https://adventofcode.com/2020)
* [2021](https://adventofcode.com/2021)
* [2022](https://adventofcode.com/2022)
* [2023](https://adventofcode.com/2023)
* [2024](https://adventofcode.com/2024)
* [2025](https://adventofcode.com/2025)

How to run
------------------------------------

The `flake.nix` in the root of the repository provides a devShell for each
language, enter one at a time with `nix develop .#<language>`:

`python`, `elixir`, `rust`, `go`, `haskell`, `erlang`, `scala`, `csharp`,
`fsharp`, `c`, `cpp`, `d`, `clojure`, `dart` and `java`

The packages for each language are listed in `languages.nix`.

Scripts
------------------------------------

The scripts in the `scripts` directory are exposed as packages of the flake and
are available as commands in every devShell.

* `nix run .#fetch` - saves the puzzle description and the input for today
* `nix run .#fetch -- --next` - same, for the first day without an input
* `nix run .#fetch -- --year 2019 --day 3` - same, for a specific day
* `nix run .#fetch -- --year 2019 --day 3 --force` - downloads the description
  again, for example to add part two once part one is solved

The input and part two of a puzzle are only downloaded when the session cookie
of adventofcode.com is available in the `AOC_SESSION` environment variable or in
the `~/.config/aoc/session` file.  Never commit the session cookie.

The puzzle descriptions and inputs are copyright
[Advent of Code](https://adventofcode.com), each downloaded README names its
source.  Advent of Code asks that they are not redistributed.

What to know
------------------------------------

* **Session cookie** - the inputs and part two of each puzzle need the session
  cookie of adventofcode.com in the `AOC_SESSION` environment variable or in the
  `~/.config/aoc/session` file.  The downloaded READMEs only contain part one
  and no inputs were downloaded for them.
* **Git tracking** - nix only sees files that are tracked by git, new files need
  a `git add` before `nix develop .#<language>` or `nix run .#fetch` find them.
* **devShells** - every devShell evaluates, but only `python` and `go` have been
  built and entered so far.  The others are several GB of downloads the first
  time they are used.
* **Redistribution** - Advent of Code asks that the puzzle text and the inputs
  are not republished, the source note in each README does not change that.
  Keep the downloaded READMEs and inputs out of a public repository.
* **Automated requests** - Advent of Code asks scripts to identify their owner,
  set `AOC_USER_AGENT` to include contact details as the default is generic.

Tasks
------------------------------------

* [ ] Remove `2015/template/day-01`, it duplicates `2015/day1`
* [ ] Rename `2019/day-01` and `2019/day-02` to `2019/day1` and `2019/day2`,
      and their `puzzle-input.txt` to `input.txt`
* [ ] Rename `2020/01` to `2020/day1`
* [ ] Fill in the `Days` list of `2015/README.md`, `2016/README.md` and
      `2020/README.md` like the other years
* [ ] Build the remaining devShells to confirm they work
* [ ] Decide if the downloaded READMEs and inputs should be ignored by git

Events
---------------------------

Advent of code has been running since 2015.

[Advent of Code Events](https://adventofcode.com/events)
