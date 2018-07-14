import React from "react";

import NewsThumbnail from "./NewsThumbnail";
import NewsTimestamp from "./NewsTimestamp";
import NewsHeadline from "./NewsHeadline";
import NewsExcerpt from "./NewsExcerpt";
import "./newsBlockLayout.css";

export default class NewsBlockLayout extends React.Component {

    constructor(props) {
        super(props);
        this.state = { mouseHover: false };
    }

    handleOnMouseEnter() {
        this.setState({ mouseHover: true });
    }

    handleOnMouseLeave() {
        this.setState({ mouseHover: false })
    }

    render() {
        var thumbnail = null;
        if (this.props.thumbnailUrl) {
            thumbnail = <NewsThumbnail src={this.props.thumbnailUrl} />;
        }
        return (
            <div styleName="news-block"
                onMouseEnter={this.handleOnMouseEnter.bind(this)}
                onMouseLeave={this.handleOnMouseLeave.bind(this)}>
                <a styleName="header-anchor" href={this.props.url}>
                    {thumbnail}
                    <NewsTimestamp hovering={this.state.mouseHover}>{this.props.timestamp}</NewsTimestamp>
                    <NewsHeadline hovering={this.state.mouseHover}>{this.props.headline}</NewsHeadline>
                </a>
                <a styleName="excerpt-anchor" href={this.props.url}>
                    <NewsExcerpt hovering={this.state.mouseHover}>{this.props.excerpt}</NewsExcerpt>
                </a>
            </div>
        );
    }
}