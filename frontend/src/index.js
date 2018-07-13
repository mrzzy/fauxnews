import React from "react";
import ReactDOM from "react-dom";
import HomeLayout from "./home/HomeLayout";

class MainLayout extends React.Component {
    render() {
        return (
            <HomeLayout />
        );
    }
}

const app = document.getElementById("app");
ReactDOM.render(<MainLayout />, app);