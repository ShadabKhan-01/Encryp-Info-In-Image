'use client';
import React from 'react';
import styled from '@emotion/styled';

const Card = ({Text}) => {
  return (
    <StyledWrapper>
      <div className="bgblue">
        <div className="card">
          {Text}
        </div>
      </div>
    </StyledWrapper>
  );
};

const StyledWrapper = styled.div`
  .bgblue {
    background: linear-gradient(135deg, #fffffff5, #3a4b8a, #ffffff98);
    padding: 1px;
    border-radius: 1.2rem;
    box-shadow: 0px 1rem 1.5rem -0.9rem #000000e1;
    max-width: 300px;
  }

  .card {
    font-size: 1rem;
    color: #bec4cf;
    background: linear-gradient(135deg, #0d1120 0%, #3a4b8a 43%, #0d1120 100%);
    padding: 1.5rem;
    border-radius: 1.2rem;
  }
`;

export default Card;
