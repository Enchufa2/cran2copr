%global packname  sptotal
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}%{?buildtag}
Summary:          Predicting Totals and Weighted Sums from Spatial Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-sp 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-viridis 
Requires:         R-graphics 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-sp 

%description
Performs predictions of totals and weighted sums, or finite population
block kriging, on spatial data using the methods in Ver Hoef (2008)
<doi:10.1007/s10651-007-0035-y>. The primary outputs are an estimate of
the total, mean, or weighted sum in the region, an estimated prediction
variance, and a plot of the predicted and observed values. This is useful
primarily to users with ecological data that are counts or densities
measured on some sites in a finite area of interest. Spatial prediction
for the total count or average density in the entire region can then be
done using the functions in this package.

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
