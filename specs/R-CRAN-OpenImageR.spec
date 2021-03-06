%global packname  OpenImageR
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          3%{?dist}%{?buildtag}
Summary:          An Image Processing Toolkit

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-RcppArmadillo >= 0.8.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.17
BuildRequires:    R-graphics 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-tiff 
BuildRequires:    R-CRAN-R6 
Requires:         R-CRAN-Rcpp >= 0.12.17
Requires:         R-graphics 
Requires:         R-grid 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-png 
Requires:         R-CRAN-tiff 
Requires:         R-CRAN-R6 

%description
Incorporates functions for image preprocessing, filtering and image
recognition. The package takes advantage of 'RcppArmadillo' to speed up
computationally intensive functions. The histogram of oriented gradients
descriptor is a modification of the 'findHOGFeatures' function of the
'SimpleCV' computer vision platform, the average_hash(), dhash() and
phash() functions are based on the 'ImageHash' python library. The Gabor
Feature Extraction functions are based on 'Matlab' code of the paper,
"CloudID: Trustworthy cloud-based and cross-enterprise biometric
identification" by M. Haghighat, S. Zonouz, M. Abdel-Mottaleb, Expert
Systems with Applications, vol. 42, no. 21, pp. 7905-7916, 2015,
<doi:10.1016/j.eswa.2015.06.025>. The 'SLIC' and 'SLICO' superpixel
algorithms were explained in detail in (i) "SLIC Superpixels Compared to
State-of-the-art Superpixel Methods", Radhakrishna Achanta, Appu Shaji,
Kevin Smith, Aurelien Lucchi, Pascal Fua, and Sabine Suesstrunk, IEEE
Transactions on Pattern Analysis and Machine Intelligence, vol. 34, num.
11, p. 2274-2282, May 2012, <doi:10.1109/TPAMI.2012.120> and (ii) "SLIC
Superpixels", Radhakrishna Achanta, Appu Shaji, Kevin Smith, Aurelien
Lucchi, Pascal Fua, and Sabine Suesstrunk, EPFL Technical Report no.
149300, June 2010.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/COPYRIGHTS
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/include
%doc %{rlibdir}/%{packname}/shiny_app
%doc %{rlibdir}/%{packname}/tmp_images
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
