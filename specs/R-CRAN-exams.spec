%global packname  exams
%global packver   2.3-4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.4
Release:          1%{?dist}
Summary:          Automatic Generation of Exams in R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-tools 
Requires:         R-utils 

%description
Automatic generation of exams based on exercises in Markdown or LaTeX
format, possibly including R code for dynamic generation of exercise
elements. Exercise types include single-choice and multiple-choice
questions, arithmetic problems, string questions, and combinations thereof
(cloze). Output formats include standalone files (PDF, HTML, Docx, ODT,
...), Moodle XML, QTI 1.2, QTI 2.1, Blackboard, Canvas, OpenOLAT, ARSnova,
and TCExam. In addition to fully customizable PDF exams, a standardized
PDF format (NOPS) is provided that can be printed, scanned, and
automatically evaluated.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/exercises
%doc %{rlibdir}/%{packname}/nops
%doc %{rlibdir}/%{packname}/pandoc
%doc %{rlibdir}/%{packname}/tex
%doc %{rlibdir}/%{packname}/xml
%{rlibdir}/%{packname}/INDEX