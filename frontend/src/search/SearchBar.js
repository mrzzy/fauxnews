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
        <div className="input-group" styleName="search-bar">
            <input className="form-control py-2 border-right-0 border"
                type="search" placeholder="search" onKeyPress={this.handleOnKeyPress.bind(this)} />
            <span className="input-group-append">
                <div className="input-group-text bg-transparent">
                    <i className="fa fa-search"></i>
                </div>
            </span>
        </div>);
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