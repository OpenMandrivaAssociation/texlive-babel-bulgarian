%global tl_name babel-bulgarian
%global tl_revision 31902

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2g
Release:	%{tl_revision}.1
Summary:	Babel contributed support for Bulgarian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/bulgarian
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for documents in Bulgarian (or simply
containing some Bulgarian text).

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
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-bulgarian
%dir %{_datadir}/texmf-dist/source/generic/babel-bulgarian
%dir %{_datadir}/texmf-dist/tex/generic/babel-bulgarian
%doc %{_datadir}/texmf-dist/doc/generic/babel-bulgarian/README
%doc %{_datadir}/texmf-dist/doc/generic/babel-bulgarian/bulgarian.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-bulgarian/bulgarian.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-bulgarian/bulgarian.ins
%{_datadir}/texmf-dist/tex/generic/babel-bulgarian/bulgarian.ldf
