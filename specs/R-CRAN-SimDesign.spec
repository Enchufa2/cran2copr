%global packname  SimDesign
%global packver   2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Structure for Organizing Monte Carlo Simulation Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-pbapply >= 1.3.0
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-pbapply >= 1.3.0
Requires:         R-CRAN-foreach 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 

%description
Provides tools to help safely and efficiently organize Monte Carlo
simulations in R. The package controls the structure and back-end of Monte
Carlo simulations by utilizing a general generate-analyse-summarise
strategy. The functions provided control common simulation issues such as
re-simulating non-convergent results, support parallel back-end and MPI
distributed computations, save and restore temporary files, aggregate
results across independent nodes, and provide native support for
debugging. For a pedagogical introduction to the package refer to Sigal
and Chalmers (2016) <doi:10.1080/10691898.2016.1246953>, and for an
in-depth overview of the package and its design philosophy see Chalmers
and Adkins (2020) <doi:10.20982/tqmp.16.4.p248>.

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
