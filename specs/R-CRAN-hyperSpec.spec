%global packname  hyperSpec
%global packver   0.99-20180627
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.20180627
Release:          1%{?dist}
Summary:          Work with Hyperspectral Data, i.e. Spectra + Meta Information(Spatial, Time, Concentration, ...)

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 2.2.0
BuildRequires:    R-lattice 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-lazyeval 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-ggplot2 >= 2.2.0
Requires:         R-lattice 
Requires:         R-grid 
Requires:         R-CRAN-testthat 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-lazyeval 
Requires:         R-CRAN-XML 

%description
Comfortable ways to work with hyperspectral data sets. I.e. spatially or
time-resolved spectra, or spectra with any other kind of information
associated with each of the spectra. The spectra can be data as obtained
in XRF, UV/VIS, Fluorescence, AES, NIR, IR, Raman, NMR, MS, etc. More
generally, any data that is recorded over a discretized variable, e.g.
absorbance = f (wavelength), stored as a vector of absorbance values for
discrete wavelengths is suitable.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX