#!/usr/local/bin/perl

use English;
use Cwd;
$classpath="/Users/qaauto/Desktop/email";
$currdir=getcwd();

$conf=shift(@ARGV);
$release=shift(@ARGV);
$product=shift(@ARGV);
$pkgname=shift(@ARGV);
$suite = shift(@ARGV);
$br=shift(@ARGV);
$testrailpath = shift(@ARGV);
$contacts=shift(@ARGV);
$result_report=$currdir."/qa/selenium/".${suite}."/results/test_results.txt";

$mailgp="arif_bhuiyan\@ibi.com";
$contacts="$mailgp".","."$contacts";
$from="qaauto\@ibi.com";
$sub="\"$suite run results for $product $release $conf $pkgname with $br\"";
$message="\"$testrailpath\"";
$cmd="java -cp $classpath emailtogp $contacts $from  $sub $message $result_report";
print "$cmd\n";
system($cmd);
