%global packname  hisse
%global packver   1.9.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.18
Release:          1%{?dist}%{?buildtag}
Summary:          Hidden State Speciation and Extinction

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-GenSA 
BuildRequires:    R-CRAN-subplex 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-diversitree 
BuildRequires:    R-CRAN-plotrix 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-GenSA 
Requires:         R-CRAN-subplex 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-data.table 
Requires:         R-methods 
Requires:         R-CRAN-diversitree 
Requires:         R-CRAN-plotrix 

%description
Sets up and executes a HiSSE model (Hidden State Speciation and
Extinction) on a phylogeny and character sets to test for hidden shifts in
trait dependent rates of diversification. Beaulieu and O'Meara (2016)
<doi:10.1093/sysbio/syw022>.

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
