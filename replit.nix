{pkgs}: {
  deps = [
    pkgs.nodePackages.prettier
    pkgs.rustc
    pkgs.pkg-config
    pkgs.libiconv
    pkgs.cargo
    pkgs.zlib
    pkgs.tk
    pkgs.tcl
    pkgs.openjpeg
    pkgs.libxcrypt
    pkgs.libwebp
    pkgs.libtiff
    pkgs.libjpeg
    pkgs.libimagequant
    pkgs.lcms2
    pkgs.freetype
    pkgs.tesseract
    pkgs.openssl
    pkgs.postgresql
  ];
}
