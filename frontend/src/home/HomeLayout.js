import React from "react";
import axios from "axios";

import NewsBlockLayout from "../newsblock/NewsBlockLayout";
import HeaderLayout from "../header/HeaderLayout";

import "./homeLayout.css";
import RailsNewsLayout from "../news_columns/RailsNewsLayout";

export default class HomeLayout extends React.Component {
    constructor(props) {
        super(props);
        this.state = { shownLayouts: [] };
    }

    render() {
        return (
            <div className="container">
                <HeaderLayout />
                <RailsNewsLayout>
                    {this.state.shownLayouts}
                </RailsNewsLayout>
            </div>
        );
    }

    componentDidMount() {
        axios.get("http://127.0.0.1:8000/api/articles/", {
                headers: {
                    'Access-Control-Request-Method': 'GET',
                    "Access-Control-Request-Headers": "Content-Type"
                }
            }
        ).then((response) => {
            var layouts = [];
            for (var i=0; i<response.data.length; i++) {
                var d = response.data[i];
                layouts.push(
                    <NewsBlockLayout key={i} thumbnailUrl={d["thumbnail_url"]}
                        timestamp={d["datePublished"]} headline={d["title"]}
                        excerpt={d["excerpt"]} url={d["url"]} />
                );
            }
            this.setState({ shownLayouts: layouts });
        });
    }
}