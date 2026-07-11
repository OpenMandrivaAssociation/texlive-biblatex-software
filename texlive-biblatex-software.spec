%global tl_name biblatex-software
%global tl_revision 77180

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2~8
Release:	%{tl_revision}.1
Summary:	BibLaTeX stylefiles for software products
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-software
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-software.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-software.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-software.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements software entry types for BibLaTeX in the form of
a bibliography style extension. It requires the Biber backend.

