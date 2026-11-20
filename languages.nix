{pkgs}: let
  beam = pkgs.beam.packages.erlang;
  dotnet = {
    packages = [pkgs.dotnet-sdk];
    env = [
      {
        name = "DOTNET_CLI_TELEMETRY_OPTOUT";
        value = "1";
      }
    ];
  };
  native = with pkgs; [
    gcc
    gnumake
    cmake
    pkg-config
    gdb
    clang-tools
  ];
in {
  python.packages = [
    (pkgs.python3.withPackages (pypkgs: [
      pypkgs.click
      pypkgs.pytest
    ]))
    pkgs.ruff
  ];

  elixir.packages = [
    beam.elixir
    beam.erlang
    beam.hex
  ];

  rust.packages = with pkgs; [
    cargo
    rustc
    clippy
    rustfmt
    rust-analyzer
    gcc
  ];

  go.packages = with pkgs; [
    go
    gopls
  ];

  haskell.packages = with pkgs; [
    ghc
    cabal-install
    haskell-language-server
  ];

  erlang.packages = [
    beam.erlang
    beam.rebar3
  ];

  scala.packages = with pkgs; [
    jdk
    scala
    sbt
    scala-cli
  ];

  csharp = dotnet;

  fsharp =
    dotnet
    // {
      packages = dotnet.packages ++ [pkgs.fantomas];
    };

  c.packages = native;

  cpp.packages = native;

  d.packages = with pkgs; [
    ldc
    dub
  ];

  clojure.packages = with pkgs; [
    jdk
    clojure
    leiningen
    babashka
  ];

  dart.packages = [pkgs.dart];

  java.packages = with pkgs; [
    jdk
    maven
    gradle
  ];
}
