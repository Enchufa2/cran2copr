%global packname  serp
%global packver   0.1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.8
Release:          1%{?dist}%{?buildtag}
Summary:          Smooth Effects on Response Penalty for 'CLM'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ordinal >= 2016.12.12
BuildRequires:    R-stats 
Requires:         R-CRAN-ordinal >= 2016.12.12
Requires:         R-stats 

%description
A regularization method for the cumulative link models.  The
'smooth-effect-on-response penalty' ('SERP') provides flexible modelling
of the ordinal model by enabling the smooth transition from the general
cumulative link model to a coarser form of the same model. In other words,
as the tuning parameter goes from zero to infinity, the subject-specific
effects associated with each variable in the model tend to a unique global
effect. The parameter estimates of the general cumulative model are mostly
unidentifiable or at least only identifiable within a range of the entire
parameter space. Thus, by maximizing a penalized rather than the usual
non-penalized log-likelihood, this and other numerical problems common
with the general model are to a large extent eliminated. Fitting is via a
modified Newton's method. Several standard model performance and
descriptive methods are also available. An outline of the penalty
implemented here is found in Tutz, G and Gertheiss, J (2016)
<doi:10.1177/1471082X16642560>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
