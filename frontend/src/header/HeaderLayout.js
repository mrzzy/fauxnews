import React from "react";

import Subtitle from "../common/Subtitle";
import RailsLayout from "../common/RailsLayout";

import FaintSubtitle from "./FaintSubtitle";
import ImageHeading from "./ImageHeading";

import "./headerLayout.css";

export default class HeaderLayout extends React.Component {
    render() {
        return (
            <div styleName="container">
                <ImageHeading src="./res/imgs/heading.png" />
                    <div styleName="subheading">
                        <RailsLayout>
                            <FaintSubtitle alignLeft>13 July 2018</FaintSubtitle>
                            <Subtitle alignCenter>The most questionable news source</Subtitle>
                            <FaintSubtitle alignRight>International</FaintSubtitle>
                        </RailsLayout>
                    </div>
                <hr />
            </div>
        );
    }
}