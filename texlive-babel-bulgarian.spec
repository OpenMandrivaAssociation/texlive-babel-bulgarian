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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for documents in Bulgarian (or simply
containing some Bulgarian text).

