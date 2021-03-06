%global packname  SightabilityModel
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Wildlife Sightability Modeling

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-formula.tools 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-utils 
Requires:         R-CRAN-formula.tools 
Requires:         R-Matrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-plyr 
Requires:         R-stats 
Requires:         R-CRAN-survey 
Requires:         R-utils 

%description
Uses logistic regression to model the probability of detection as a
function of covariates. This model is then used with observational survey
data to estimate population size, while accounting for uncertain
detection.  See Steinhorst and Samuel (1989).

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
