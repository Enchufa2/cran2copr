%global packname  rtide
%global packver   0.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.7
Release:          2%{?dist}
Summary:          Tide Heights

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-chk >= 0.4.0
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-dttr2 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-chk >= 0.4.0
Requires:         R-CRAN-abind 
Requires:         R-CRAN-dttr2 
Requires:         R-utils 
Requires:         R-CRAN-tibble 

%description
Calculates tide heights based on tide station harmonics. It includes the
harmonics data for 637 US stations. The harmonics data was converted from
<https://github.com/poissonconsulting/rtide/blob/master/data-raw/harmonics-dwf-20151227-free.tar.bz2>,
NOAA web site data processed by David Flater for 'XTide'. The code to
calculate tide heights from the harmonics is based on 'XTide'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
