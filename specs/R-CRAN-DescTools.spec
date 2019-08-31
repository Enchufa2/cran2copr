%global packname  DescTools
%global packver   0.99.28
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.28
Release:          1%{?dist}
Summary:          Tools for Descriptive Statistics

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.10
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-MASS 
BuildRequires:    R-utils 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-manipulate 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.10
Requires:         R-base 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-MASS 
Requires:         R-utils 
Requires:         R-boot 
Requires:         R-CRAN-manipulate 
Requires:         R-CRAN-mvtnorm 
Requires:         R-foreign 
Requires:         R-CRAN-expm 

%description
A collection of miscellaneous basic statistic functions and convenience
wrappers for efficiently describing data. The author's intention was to
create a toolbox, which facilitates the (notoriously time consuming) first
descriptive tasks in data analysis, consisting of calculating descriptive
statistics, drawing graphical summaries and reporting the results. The
package contains furthermore functions to produce documents using MS Word
(or PowerPoint) and functions to import data from Excel. Many of the
included functions can be found scattered in other packages and other
sources written partly by Titans of R. The reason for collecting them
here, was primarily to have them consolidated in ONE instead of dozens of
packages (which themselves might depend on other packages which are not
needed at all), and to provide a common and consistent interface as far as
function and arguments naming, NA handling, recycling rules etc. are
concerned. Google style guides were used as naming rules (in absence of
convincing alternatives). The 'camel style' was consequently applied to
functions borrowed from contributed R packages as well.

%prep
%setup -q -c -n %{packname}


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
%{rlibdir}/%{packname}/data
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs