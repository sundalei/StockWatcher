package com.google.gwt.sample.stockwatcher;

import java.io.Serializable;

public class DelistedException extends Exception implements Serializable {
    
    private String symbol;

    public DelistedException() {

    }

    public DelistedException(String symbol) {
        this.symbol = symbol;
    }

    public String getSymbol() {
        return this.symbol;
    }
}