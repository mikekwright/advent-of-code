{
  description = "Advent of Code - a devShell per language and the helper scripts";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-parts = {
      url = "github:hercules-ci/flake-parts";
      inputs.nixpkgs-lib.follows = "nixpkgs";
    };

    devshell = {
      url = "github:numtide/devshell";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {flake-parts, ...} @ inputs:
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
        lib,
        ...
      }: let
        scripts = import ./scripts {inherit pkgs;};
        languages = import ./languages.nix {inherit pkgs;};

        scriptCommands =
          map (script: {
            package = script;
            category = "advent of code";
          })
          (builtins.attrValues scripts);

        languageShell = name: language: {
          name = "aoc-${name}";
          commands = scriptCommands;
          packages = language.packages;
          env = language.env or [];
        };
      in {
        packages = scripts;

        devshells =
          {
            default = {
              name = "aoc";
              commands = scriptCommands;
            };
          }
          // lib.mapAttrs languageShell languages;
      };
    };
}
