import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

const useScrollQuiz = (pageNumber, quizType) => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [quizes, setQuizes] = useState([]);
  const [hasMore, setHasMore] = useState(false);

  useEffect(() => {
    setQuizes([]);
  }, [quizType]);

  useEffect(() => {
    setLoading(true);
    axios
      .get("/api/admin/showpreview", {
        transitional: {
          silentJSONParsing: false,
        },
        responseType: "json",
        params: {
          quiz_type: quizType,
          page: pageNumber,
        },
      })
      .then((response) => {
        console.log(response);
        const quizes = JSON.parse(response.data.quizes);
        console.log(quizes);
        setQuizes((prevQuizes) => {
          return [...new Set([...prevQuizes, ...quizes.map((b) => b.quiz_id)])];
        });
        setHasMore(quizes.length > 0);
        setLoading(false);
      })
      .catch((e) => setError(e));
  }, [pageNumber, quizType]);

  return { loading, error, quizes, hasMore };
};

export default useScrollQuiz;
