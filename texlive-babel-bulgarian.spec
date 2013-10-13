# revision 30258
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-babel-bulgarian
Version:	20131013
Release:	1
Summary:	TeXLive babel-bulgarian package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-bulgarian package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-bulgarian/bulgarian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-bulgarian/bulgarian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-bulgarian/bulgarian.dtx
%doc %{_texmfdistdir}/source/generic/babel-bulgarian/bulgarian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
