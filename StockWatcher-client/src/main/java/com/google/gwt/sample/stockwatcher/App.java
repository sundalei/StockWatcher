package com.google.gwt.sample.stockwatcher;

import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.core.client.GWT;
import com.google.gwt.user.client.ui.Button;
import com.google.gwt.user.client.ui.FlexTable;
import com.google.gwt.user.client.ui.HorizontalPanel;
import com.google.gwt.user.client.ui.Label;
import com.google.gwt.user.client.ui.TextBox;
import com.google.gwt.user.client.ui.VerticalPanel;

/**
 * Entry point classes define <code>onModuleLoad()</code>.
 */
public class App implements EntryPoint {
	private VerticalPanel mainPanel = new VerticalPanel();

	private FlexTable stocksFlexTable = new FlexTable();

	private HorizontalPanel addPanel = new HorizontalPanel();

	private TextBox newSymbolTextBox = new TextBox();

	private Button addStockButton = new Button("Add");

	private Label lastUpdatedLabel = new Label();

	/**
	 * The message displayed to the user when the server cannot be reached or returns an error.
	 */
	private static final String SERVER_ERROR = "An error occurred while "
	                + "attempting to contact the server. Please check your network " + "connection and try again.";

	/**
	 * Create a remote service proxy to talk to the server-side Greeting service.
	 */
	private final GreetingServiceAsync greetingService = GWT.create(GreetingService.class);

	/**
	 * Entry point method.
	 */
	@Override
	public void onModuleLoad() {
		// TODO Create table for stock data.
		// TODO Assemble Add Stock panel.
		// TODO Assemble Main panel.
		// TODO Associate the Main panel with the HTML page.
		// TODO Move cursor focus to the input box.
	}
}
