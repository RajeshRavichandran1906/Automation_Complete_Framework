#!/usr/local/bin/perl
$classpath="\\\\bigrepos01\\bigscm\\admin\\bin";

$conf=shift(@ARGV);
$release=shift(@ARGV);
$product=shift(@ARGV);
$pkgname=shift(@ARGV);
$suite = shift(@ARGV);
$br=shift(@ARGV);
$testrailpath = shift(@ARGV);
$contacts=shift(@ARGV);
#$cmd="phantomjs c:\\testrail.js $suite \"$testrailpath\"";
#print "$cmd\n";
#system($cmd);

$from="qaauto\@ibi.com";
$sub="\"$suite run results for $product $release $conf $pkgname with $br\"";
$message="\"$testrailpath\"";
#$report="c:\\\\temp\\\\${suite}.png";
#$cmd="java   -cp $classpath emailtogp $contacts $from  $sub $message $report";
$cmd="java   -cp $classpath emailtogp $contacts $from  $sub $message";
print "$cmd\n";
system($cmd);


