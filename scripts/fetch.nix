{
  writeShellApplication,
  coreutils,
  curl,
  git,
  gnugrep,
  gnused,
  pandoc,
}:
writeShellApplication {
  name = "aoc-fetch";
  runtimeInputs = [
    coreutils
    curl
    git
    gnugrep
    gnused
    pandoc
  ];
  text = builtins.readFile ./fetch.sh;
  meta.description = "Save the puzzle description and download the input for an Advent of Code day";
}
