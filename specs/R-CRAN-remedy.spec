%global packname  remedy
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          'RStudio' Addins to Simplify 'Markdown' Writing

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-rematch2 
BuildRequires:    R-utils 
BuildRequires:    R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-rematch2 
Requires:         R-utils 
Requires:         R-stats 

%description
An 'RStudio' addin providing shortcuts for writing in 'Markdown'. This
package provides a series of functions that allow the user to be more
efficient when using 'Markdown'. For example, you can select a word, and
put it in bold or in italics, or change the alignment of elements inside
you Rmd. The idea is to map all the functionalities from 'remedy' on
keyboard shortcuts, so that it provides an interface close to what you can
find in any other text editor.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/rstudio
%{rlibdir}/%{packname}/INDEX
