Name:		texlive-biblatex-software
Version:	64030
Release:	1
Summary:	BibLaTeX stylefiles for software products
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-software
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-software.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-software.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-software.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package implements software entry types for BibLaTeX in
the form of a bibliography style extension. It requires the
Biber backend.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/biblatex-software
%{_texmfdistdir}/tex/latex/biblatex-software
%doc %{_texmfdistdir}/doc/latex/biblatex-software

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
