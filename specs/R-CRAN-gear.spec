%global packname  gear
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          Geostatistical Analysis in R

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-autoimage 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
Requires:         R-CRAN-autoimage 
Requires:         R-lattice 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-CRAN-optimx 

%description
Implements common geostatistical methods in a clean, straightforward,
efficient manner. The methods are discussed in Schabenberger and Gotway
(2004, <ISBN:9781584883227>) and Waller and Gotway (2004,
<ISBN:9780471387718>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/testdata-raw
%{rlibdir}/%{packname}/INDEX
