%global packname  RAthena
%global packver   1.10.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Connect to 'AWS Athena' using 'Boto3' ('DBI' Interface)

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.13
BuildRequires:    R-CRAN-data.table >= 1.12.4
BuildRequires:    R-CRAN-DBI >= 0.7
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-reticulate >= 1.13
Requires:         R-CRAN-data.table >= 1.12.4
Requires:         R-CRAN-DBI >= 0.7
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Designed to be compatible with the R package 'DBI' (Database Interface)
when connecting to Amazon Web Service ('AWS') Athena
<https://aws.amazon.com/athena/>. To do this 'Python' 'Boto3' Software
Development Kit ('SDK')
<https://boto3.amazonaws.com/v1/documentation/api/latest/index.html> is
used as a driver.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
