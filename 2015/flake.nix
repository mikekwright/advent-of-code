{
  description = "Flake for the python setup to work with Advent of Code 2015";

  inputs = {
    # NixPkgs - Unstable on 2025-02-08
    nixpkgs.url = "github:nixos/nixpkgs/a79cfe0ebd24952b580b1cf08cd906354996d547";
    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs.follows = "nixpkgs";
    };

    devshell = {
      url = "github:numtide/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    flake-parts,
    ...
  } @ inputs:
    flake-parts.lib.mkFlake {inherit inputs;} {
      imports = [
        inputs.devshell.flakeModule
      ];

      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      perSystem = {
        pkgs,
        ...
      }: 
        let
          # NixOS wiki on setting up python - https://nixos.wiki/wiki/Python
          python-config = pkgs.python3.withPackages (pypkgs: [
            pypkgs.click
            pypkgs.pytest
          ]);
        in
        {
          devshells.default = {
            env = [{
              name = "AOC";
              value = 2015;
            }];

            commands = [
              (import (./day1/command.nix))
              (import (./day2/command.nix))
              (import (./day3/command.nix))
              (import (./day4/command.nix))
            ];

            packages = [
              python-config
            ];
          };

          packages = {
            default = python-config;
          };
        };
      };
}
