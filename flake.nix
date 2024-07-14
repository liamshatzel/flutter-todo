{
    inputs = {
        nixpkgs.url = "nixpkgs/nixos-24.05";
        flake-utils.url = "github:numtide/flake-utils";
    };

    outputs = { self, nixpkgs, flake-utils } @ inputs:
    flake-utils.lib.eachDefaultSystem (system:
    let
        pkgs = import inputs.nixpkgs {
            inherit system;
            config = {
                allowUnfree = true;
            };
        };
    in
    {
        devShell = 
            with pkgs; mkShell rec {
                buildInputs = with pkgs; [
                    (python312.withPackages (ps: with ps; [
                        flask
                        pip
                    ]))
                        nodePackages.prettier
                        nodePackages.pyright
                ];

                shellHook = ''
                    fish
                    '';
            };
    });
}

