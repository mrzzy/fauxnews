import React from "react";

import "./searchBar.css";

export default class SearchBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            search: this.createSearch()
        };
    }

    createSearch() {
        return (
            <input type="text" styleName="search-bar" placeholder="Find the most reliable news..."
                onKeyPress={this.handleOnKeyPress.bind(this)} />
        );
    }

    showSearch() {
        this.setState({
            search: this.createSearch()
        });
    }

    handleOnKeyPress(event) {
        if (event.key === "Enter") {
            this.setState({
                search: <div>
                    <p>Please press CTRL+F or ⌘+F and type {event.target.value}</p>
                    <p styleName="search-again" onClick={this.showSearch.bind(this)}>Make another search</p>
                </div>
            });
        }
    }

    render() {
        return (
            <div>
                {this.state.search}
            </div>
        );
    }
}