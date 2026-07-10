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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package implements software entry types for BibLaTeX in the form of
a bibliography style extension. It requires the Biber backend.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-software
%dir %{_datadir}/texmf-dist/source/latex/biblatex-software
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-software
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/Changes
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/biblio.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/history.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/manual.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/mkbiblatexstubs.sh
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/sample-content.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/sample-use-sty.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/sample-use-sty.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/sample.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/showcase-crossref.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/showcase-crossref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/showcase-crossref.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/software-biblatex.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/software-biblatex.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/stublist
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-software/swentries.tex
%doc %{_datadir}/texmf-dist/source/latex/biblatex-software/Makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-software/english-software.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-software/french-software.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-software/software-biblatex.sty
%{_datadir}/texmf-dist/tex/latex/biblatex-software/software.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-software/software.dbx
