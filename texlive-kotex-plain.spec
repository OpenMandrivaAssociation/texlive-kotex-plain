# revision 32104
# category Package
# catalog-ctan /language/korean/kotex-plain
# catalog-date 2013-11-03 10:05:42 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-kotex-plain
Version:	20131103
Release:	3
Summary:	Macros for typesetting Korean under Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/korean/kotex-plain
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-plain.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kotex-plain.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
