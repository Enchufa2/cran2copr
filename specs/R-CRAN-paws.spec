%global packname  paws
%global packver   0.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          Amazon Web Services Software Development Kit

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-paws.compute >= 0.1.9
BuildRequires:    R-CRAN-paws.storage >= 0.1.9
BuildRequires:    R-CRAN-paws.database >= 0.1.9
BuildRequires:    R-CRAN-paws.networking >= 0.1.9
BuildRequires:    R-CRAN-paws.management >= 0.1.9
BuildRequires:    R-CRAN-paws.machine.learning >= 0.1.9
BuildRequires:    R-CRAN-paws.analytics >= 0.1.9
BuildRequires:    R-CRAN-paws.security.identity >= 0.1.9
BuildRequires:    R-CRAN-paws.application.integration >= 0.1.9
BuildRequires:    R-CRAN-paws.cost.management >= 0.1.9
BuildRequires:    R-CRAN-paws.customer.engagement >= 0.1.9
Requires:         R-CRAN-paws.compute >= 0.1.9
Requires:         R-CRAN-paws.storage >= 0.1.9
Requires:         R-CRAN-paws.database >= 0.1.9
Requires:         R-CRAN-paws.networking >= 0.1.9
Requires:         R-CRAN-paws.management >= 0.1.9
Requires:         R-CRAN-paws.machine.learning >= 0.1.9
Requires:         R-CRAN-paws.analytics >= 0.1.9
Requires:         R-CRAN-paws.security.identity >= 0.1.9
Requires:         R-CRAN-paws.application.integration >= 0.1.9
Requires:         R-CRAN-paws.cost.management >= 0.1.9
Requires:         R-CRAN-paws.customer.engagement >= 0.1.9

%description
Interface to Amazon Web Services <https://aws.amazon.com>, including
storage, database, and compute services, such as 'Simple Storage Service'
('S3'), 'DynamoDB' 'NoSQL' database, and 'Lambda' functions-as-a-service.

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
