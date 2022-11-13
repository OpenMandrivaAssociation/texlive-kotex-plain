Name:		texlive-kotex-plain
Version:	63689
Release:	1
Summary:	Macros for typesetting Korean under Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/korean/kotex-plain
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-plain.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-plain.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros for typesetting Hangul, the native
alphabet of the Korean language, using plain *TeX. Input Korean
text should be encoded in UTF-8. The package is belongs to the
ko.TeX bundle.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/kotex-plain/hangulcweb.tex
%{_texmfdistdir}/tex/plain/kotex-plain/kotexplain.tex
%{_texmfdistdir}/tex/plain/kotex-plain/kotexutf-core.tex
%{_texmfdistdir}/tex/plain/kotex-plain/kotexutf.tex
%doc %{_texmfdistdir}/doc/plain/kotex-plain/ChangeLog
%doc %{_texmfdistdir}/doc/plain/kotex-plain/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
