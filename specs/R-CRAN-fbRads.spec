%global packname  fbRads
%global packver   0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Analyzing and Managing Facebook Ads from R

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-futile.logger 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-futile.logger 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-data.table 

%description
Wrapper functions around the Facebook Marketing 'API' to create, read,
update and delete custom audiences, images, campaigns, ad sets, ads and
related content.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
