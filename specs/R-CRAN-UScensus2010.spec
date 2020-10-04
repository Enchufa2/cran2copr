%global packname  UScensus2010
%global packver   0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.11
Release:          3%{?dist}%{?buildtag}
Summary:          US Census 2010 Suite of R Packages

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-foreign 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-base 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-maptools 
Requires:         R-CRAN-sp 
Requires:         R-foreign 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-base 
Requires:         R-stats 
Requires:         R-utils 

%description
US Census 2010 shape files and additional demographic data from the SF1
100 percent files. This package contains a number of helper functions for
the UScensus2010blk, UScensus2010blkgrp, UScensus2010tract,
UScensus2010cdp packages.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
