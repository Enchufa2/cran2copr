%global packname  flextable
%global packver   0.5.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.11
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Tabular Reporting

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-officer >= 0.3.13
BuildRequires:    R-CRAN-gdtools >= 0.1.6
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-uuid 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-base64enc 
Requires:         R-CRAN-officer >= 0.3.13
Requires:         R-CRAN-gdtools >= 0.1.6
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-uuid 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-base64enc 

%description
Create pretty tables for 'HTML', 'Microsoft Word' and 'Microsoft
PowerPoint' documents. Functions are provided to let users create tables,
modify and format their content. It extends package 'officer' that does
not contain any feature for customized tabular reporting and can be used
within R markdown documents.

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
