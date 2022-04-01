package com.codewithmosh;

import java.text.NumberFormat;

public class Main43java {
	
	public static void main(String[] args) {
		NumberFormat percent = NumberFormat.getPercentInstance();
		String result =  percent.format(0.1);
	    System.out.println(result);
		
	}
	
}
