Name:		texlive-babel-bulgarian
Epoch:		1
Version:	31902
Release:	2
Summary:	(Babel contributed support for Bulgarian
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/bulgarian
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-bulgarian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for documents in Bulgarian (or
simply containing some Bulgarian text).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-bulgarian/bulgarian.ldf
%doc %{_texmfdistdir}/doc/generic/babel-bulgarian/README
%doc %{_texmfdistdir}/doc/generic/babel-bulgarian/bulgarian.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-bulgarian/bulgarian.dtx
%doc %{_texmfdistdir}/source/generic/babel-bulgarian/bulgarian.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
