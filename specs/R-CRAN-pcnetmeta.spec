%global packname  pcnetmeta
%global packver   2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Patient-Centered Network Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rjags >= 4.6
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-rjags >= 4.6
Requires:         R-CRAN-coda 
Requires:         R-grDevices 
Requires:         R-methods 

%description
Performs Bayesian arm-based network meta-analysis for datasets with
binary, continuous, and count outcomes (Zhang et al., 2014
<doi:10.1177/1740774513498322>; Lin et al., 2017
<doi:10.18637/jss.v080.i05>).

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
