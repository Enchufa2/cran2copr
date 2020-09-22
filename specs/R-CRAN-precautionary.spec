%global packname  precautionary
%global packver   0.1-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Safety Diagnostics for Dose-Escalation Trial Designs

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-escalation 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-escalation 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 

%description
Enhances various R packages that support the design and simulation of
phase 1 dose-escalation trials, adding diagnostics to examine the safety
characteristics of these designs in light of expected inter-individual
variation in pharmacokinetics and pharmacodynamics. See Norris (2020),
"Retrospective analysis of a fatal dose-finding trial" <arXiv:2004.12755>.

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
