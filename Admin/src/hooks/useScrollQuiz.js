import React from "react";
import { useEffect, useState } from "react";
import axios from "axios";

const useScrollQuiz = (pageNumber, quizType) => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);
  const [quizes, setQuizes] = useState([]);
  const [quizesInfo, setQuizesInfo] = useState([]);
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
        const list_quizes = JSON.parse(response.data.quizes);
        setQuizes((prevQuizes) => {
          return [
            ...new Set([...prevQuizes, ...list_quizes.map((b) => b.quiz_id)]),
          ];
        });

        setQuizesInfo((prevInfo) => {
          return [
            ...new Set([
              ...prevInfo,
              ...list_quizes.map((b) => [b.quiz_type, b.question]),
            ]),
          ];
        });
        setHasMore(list_quizes.length > 0);
        setLoading(false);
      })
      .catch((e) => setError(e));
  }, [pageNumber, quizType]);

  return { loading, error, quizes, quizesInfo, hasMore };
};

export default useScrollQuiz;
