Name:		texlive-forest-quickstart
Version:	55688
Release:	2
Summary:	Quickstart Guide for Linguists package "forest"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/forest-quickstart
License:	fdl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forest-quickstart.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/forest-quickstart.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
forest is a PGF/TikZ-based package for drawing linguistic (and
other kinds of) trees. This manual provides a quickstart guide
for linguists with just the essential things that you need to
get started.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/forest-quickstart

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
