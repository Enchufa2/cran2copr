%global packname  ecospat
%global packver   3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Spatial Ecology Miscellaneous Methods

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-randomForest >= 4.6.7
BuildRequires:    R-CRAN-rms >= 4.5.0
BuildRequires:    R-CRAN-gtools >= 3.4.1
BuildRequires:    R-CRAN-ape >= 3.2
BuildRequires:    R-CRAN-biomod2 >= 3.1.64
BuildRequires:    R-methods >= 3.1.1
BuildRequires:    R-CRAN-maps >= 3.0.0
BuildRequires:    R-CRAN-raster >= 2.5.8
BuildRequires:    R-CRAN-vegan >= 2.4.1
BuildRequires:    R-CRAN-gbm >= 2.1.1
BuildRequires:    R-CRAN-snowfall >= 1.61
BuildRequires:    R-CRAN-ade4 >= 1.6.2
BuildRequires:    R-CRAN-foreach >= 1.4.3
BuildRequires:    R-CRAN-poibin >= 1.3
BuildRequires:    R-CRAN-ecodist >= 1.2.9
BuildRequires:    R-CRAN-ks >= 1.12.0
BuildRequires:    R-CRAN-PresenceAbsence >= 1.1.9
BuildRequires:    R-CRAN-iterators >= 1.0.8
BuildRequires:    R-CRAN-sp >= 1.0.15
BuildRequires:    R-CRAN-doParallel >= 1.0.10
BuildRequires:    R-CRAN-dismo >= 0.9.3
BuildRequires:    R-CRAN-maptools >= 0.8.39
BuildRequires:    R-CRAN-matrixStats >= 0.53.1
BuildRequires:    R-CRAN-nabor >= 0.5.0
BuildRequires:    R-CRAN-adehabitatHR >= 0.4.11
BuildRequires:    R-CRAN-adehabitatMA >= 0.3.8
BuildRequires:    R-CRAN-classInt >= 0.1.23
BuildRequires:    R-parallel 
Requires:         R-CRAN-randomForest >= 4.6.7
Requires:         R-CRAN-rms >= 4.5.0
Requires:         R-CRAN-gtools >= 3.4.1
Requires:         R-CRAN-ape >= 3.2
Requires:         R-CRAN-biomod2 >= 3.1.64
Requires:         R-methods >= 3.1.1
Requires:         R-CRAN-maps >= 3.0.0
Requires:         R-CRAN-raster >= 2.5.8
Requires:         R-CRAN-vegan >= 2.4.1
Requires:         R-CRAN-gbm >= 2.1.1
Requires:         R-CRAN-snowfall >= 1.61
Requires:         R-CRAN-ade4 >= 1.6.2
Requires:         R-CRAN-foreach >= 1.4.3
Requires:         R-CRAN-poibin >= 1.3
Requires:         R-CRAN-ecodist >= 1.2.9
Requires:         R-CRAN-ks >= 1.12.0
Requires:         R-CRAN-PresenceAbsence >= 1.1.9
Requires:         R-CRAN-iterators >= 1.0.8
Requires:         R-CRAN-sp >= 1.0.15
Requires:         R-CRAN-doParallel >= 1.0.10
Requires:         R-CRAN-dismo >= 0.9.3
Requires:         R-CRAN-maptools >= 0.8.39
Requires:         R-CRAN-matrixStats >= 0.53.1
Requires:         R-CRAN-nabor >= 0.5.0
Requires:         R-CRAN-adehabitatHR >= 0.4.11
Requires:         R-CRAN-adehabitatMA >= 0.3.8
Requires:         R-CRAN-classInt >= 0.1.23
Requires:         R-parallel 

%description
Collection of R functions and data sets for the support of spatial ecology
analyses with a focus on pre, core and post modelling analyses of species
distribution, niche quantification and community assembly. Written by
current and former members and collaborators of the ecospat group of
Antoine Guisan, Department of Ecology and Evolution (DEE) and Institute of
Earth Surface Dynamics (IDYST), University of Lausanne, Switzerland. Read
Di Cola et al. (2016) <doi:10.1111/ecog.02671> for details.

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
