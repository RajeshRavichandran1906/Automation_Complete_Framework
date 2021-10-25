#!/usr/local/bin/perl

use English;
use Cwd;
$classpath="\\\\bigrepos01\\bigscm\\admin\\bin";
$currdir=getcwd();

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
#$imageFolder=$currdir."\\qa\\selenium\\".${suite}."\\failure_captures";
#$cmd="rm -fr $imageFolder\\cvs";
#system($cmd);
#$cmd="zip -r c:\\temp\\${suite}.zip $imageFolder";
#system($cmd);

$mailgp="arif_bhuiyan\@ibi.com";
$contacts="$mailgp".","."$contacts";
$from="qaauto\@ibi.com";
$sub="\"$suite run results for $product $release $conf $pkgname with $br\"";
$message="\"$testrailpath\"";
#$report1="c:/temp/${suite}.png";
#$report2="c:/temp/${suite}.zip";
#$cmd="java   -cp $classpath emailtogp $contacts $from  $sub $message $report1 $report2";
$cmd="java   -cp $classpath emailtogp $contacts $from  $sub $message";
print "$cmd\n";
system($cmd);


