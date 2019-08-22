%global packname  AHMbook
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}
Summary:          Functions and Data for the Book 'Applied Hierarchical Modelingin Ecology'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-unmarked >= 0.12.2
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-RandomFields 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-unmarked >= 0.12.2
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-RandomFields 
Requires:         R-CRAN-coda 

%description
Provides functions and data sets to accompany the book 'Applied
Hierarchical Modeling in Ecology: Analysis of distribution, abundance and
species richness in R and BUGS' by Marc Kery and Andy Royle. The first
volume appeared early in 2016 (ISBN: 978-0-12-801378-6,
<https://www.mbr-pwrc.usgs.gov/pubanalysis/keryroylebook>); the second
volume is in preparation and additional functions will be added to this
package.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
