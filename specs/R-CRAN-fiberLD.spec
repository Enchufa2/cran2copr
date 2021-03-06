%global packname  fiberLD
%global packver   0.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          3%{?dist}%{?buildtag}
Summary:          Fiber Length Determination

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-Matrix 
Requires:         R-CRAN-VGAM 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 

%description
Routines for estimating tree fiber (tracheid) length distributions in the
standing tree based on increment core samples. Two types of data can be
used with the package, increment core data measured by means of an optical
fiber analyzer (OFA), e.g. such as the Kajaani Fiber Lab, or measured by
microscopy. Increment core data analyzed by OFAs consist of the cell
lengths of both cut and uncut fibres (tracheids) and fines (such as ray
parenchyma cells) without being able to identify which cells are cut or if
they are fines or fibres. The microscopy measured data consist of the
observed lengths of the uncut fibres in the increment core. A censored
version of a mixture of the fine and fiber length distributions is
proposed to fit the OFA data, under distributional assumptions (Svensson
et al., 2006) <doi:10.1111/j.1467-9469.2006.00501.x>. The package offers
two choices for the assumptions of the underlying density functions of the
true fiber (fine) lenghts of those fibers (fines) that at least partially
appear in the increment core, being the generalized gamma and the log
normal densities.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
